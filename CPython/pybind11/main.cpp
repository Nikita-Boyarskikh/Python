#include <pybind11/pybind11.h>

#include "library.hpp"

namespace py = pybind11;

PYBIND11_MODULE(library, m) {
    py::class_<Pet>(m, "Pet")
        .def(py::init<const std::string &>())
        .def("setName", &Pet::setName)
        .def("getName", &Pet::getName)
        .def_property("name", &Pet::getName, &Pet::setName)
        .def("__repr__", [](const Pet &a) {
            return "<library.Pet named '" + a.getName() + "'>";
        });

    py::class_<Dog, Pet>(m, "Dog")
        .def(py::init<const std::string &>())
        .def("bark", &Dog::bark)
        .def_readwrite("type", &Dog::type)
        .def("__repr__", [](const Dog &a) {
            return "<library.Dog of type '" + a.type + "' named '" + a.getName() + "'>";
        });
}
