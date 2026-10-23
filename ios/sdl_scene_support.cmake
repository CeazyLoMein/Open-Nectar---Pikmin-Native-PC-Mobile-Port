# Open Nectar's single-game-window UIScene backport for the bundled SDL2.
# Shared by production iOS builds and the asset-free simulator launch test.
target_compile_definitions(SDL2-static PRIVATE NECTAR_IOS_SCENES=1)
