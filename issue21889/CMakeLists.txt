set(I_FSOURCE fib1.f)
set(F2PYSOURCE fibby.pyf)
set(I_MODULE "fibby")

set(GENERATED_MODULE
  ${CMAKE_CURRENT_BINARY_DIR}/${I_MODULE}${PYTHON_EXTENSION_MODULE_SUFFIX})

add_custom_target(wrapper ALL DEPENDS ${I_FSOURCE})
add_custom_command(
  OUTPUT fibbymodule.c fibby-f2pywrappers.f
  COMMAND ${F2PY_EXECUTABLE} -m fibby
  ${CMAKE_CURRENT_SOURCE_DIR}/${F2PYSOURCE}
  DEPENDS ${F2PYSOURCE_DEPS} ${F2PYSOURCE}
)

add_library(
  ${I_MODULE} MODULE
  fibbymodule.c
  ${F2PY_INCLUDE_DIR}/fortranobject.c
  fibby-f2pywrappers.f
  ${I_FSOURCE})

target_include_directories(
  ${I_MODULE} PUBLIC
  ${F2PY_INCLUDE_DIRS}
  ${PYTHON_INCLUDE_DIRS}
  )

python_extension_module(${I_MODULE})

install(TARGETS ${I_MODULE} LIBRARY DESTINATION issue21889)
install(FILES ${PYSOURCE} DESTINATION issue21889)
