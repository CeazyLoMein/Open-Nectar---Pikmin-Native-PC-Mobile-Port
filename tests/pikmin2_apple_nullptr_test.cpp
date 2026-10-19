// Include the real forced adapter BEFORE the affected standard headers.
// A regression must fail here, before a full ARM64 game compilation.
#include "pikmin2_pc_types.h"
#if defined(__APPLE__) || defined(__ANDROID__)
#ifdef nullptr
#error Apple/Android must not redefine the C++ nullptr keyword
#endif
#endif
#include <type_traits>
#include <utility>
#include <unordered_map>
#include <unordered_set>
#include <vector>

struct Model {};
struct Packet {};
struct Sample { std::vector<float> matrices; };
struct Applied { Model* model; Sample saved; };

template <class T> T* forwardPointer(T* value) { return value; }
int main()
{
    static_assert(std::is_same<decltype(nullptr), std::nullptr_t>::value,
                  "nullptr must retain its native C++ type");
    Model model;
    Packet packet;
    std::vector<Model*> models;
    std::vector<Applied> applied;
    std::vector<std::vector<Packet*>> heads;
    std::vector<Packet*> callbacks;
    std::unordered_set<Model*> entered;
    std::unordered_map<Model*, Sample> current;
    models.push_back(&model);
    applied.push_back({&model, {}});
    heads.push_back({&packet});
    callbacks.push_back(nullptr);
    entered.insert(&model);
    current[&model].matrices.assign(24, 1.0f);
    auto null = nullptr;
    Model* forwarded = forwardPointer(std::forward<Model*>(static_cast<Model*>(null)));
    if (forwarded || callbacks[0] || models[0] != &model ||
        applied[0].model != &model || heads[0][0] != &packet ||
        entered.count(&model) != 1 || current.at(&model).matrices.size() != 24) return 1;
    std::puts("PASS: native nullptr and all seven affected container specializations");
}
