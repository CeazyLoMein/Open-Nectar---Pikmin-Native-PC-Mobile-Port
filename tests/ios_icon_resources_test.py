"""Configure the real iOS icon block with game targets created in child directories."""
import argparse
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def configure(cmake, source, build):
    return subprocess.run([cmake, '-S', str(source), '-B', str(build)],
                          text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cmake', default='cmake')
    args = parser.parse_args()
    source = (ROOT/'ios/CMakeLists.txt').read_text(encoding='utf-8')
    block = source[source.index('# Loose PNG icons'):source.index('message(STATUS "Experimental iOS target:')]
    with tempfile.TemporaryDirectory() as temporary:
        base = Path(temporary)
        checks = 0
        for game, target in [('pikmin1', 'pikmin_pc'), ('pikmin2', 'pikmin2_pc')]:
            fixture = base/game
            (fixture/'game').mkdir(parents=True)
            (fixture/'game/dummy.c').write_text('int main(void) { return 0; }\n')
            (fixture/'game/CMakeLists.txt').write_text(f'add_executable({target} dummy.c)\n')
            prefix = f'''cmake_minimum_required(VERSION 3.24)
project(IconScopeRegression LANGUAGES C)
set(NECTAR_IOS_GAME "{game}")
set(NECTAR_GAME_TARGET "{target}")
add_subdirectory(game)
# Execute the production block with its real icon source directory.
set(CMAKE_CURRENT_SOURCE_DIR "{(ROOT/'ios').as_posix()}")
'''
            tail = '''
get_target_property(icons ${NECTAR_GAME_TARGET} RESOURCE)
list(LENGTH icons count)
if(NOT count EQUAL 6)
    message(FATAL_ERROR "Expected six native bundle resources, got ${count}")
endif()
get_target_property(sources ${NECTAR_GAME_TARGET} SOURCES)
foreach(icon IN LISTS icons)
    if(NOT EXISTS "${icon}" OR NOT icon IN_LIST sources)
        message(FATAL_ERROR "Icon missing from target: ${icon}")
    endif()
endforeach()
'''
            cmakelists = fixture/'CMakeLists.txt'
            cmakelists.write_text(prefix+block+tail)
            result = configure(args.cmake, fixture, base/(game+'-build'))
            assert result.returncode == 0, result.stdout
            checks += 1
            # The real Build38 form must fail in the same directory structure.
            bad = block[:block.index('# The game executable')] + '''add_custom_command(TARGET ${NECTAR_GAME_TARGET} POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_if_different ${NECTAR_IOS_ICON_FILES} "$<TARGET_BUNDLE_DIR:${NECTAR_GAME_TARGET}>")
'''
            cmakelists.write_text(prefix+bad)
            result = configure(args.cmake, fixture, base/(game+'-build'))
            assert result.returncode != 0 and 'was not created in this directory' in result.stdout, result.stdout
            checks += 1
        print(f'PASS: {checks} real cross-directory icon configurations and Build38 negative controls')


if __name__ == '__main__':
    main()
