// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ps4_messages:msg/Manette.idl
// generated code does not contain a copyright notice
#include "ps4_messages/msg/detail/manette__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
ps4_messages__msg__Manette__init(ps4_messages__msg__Manette * msg)
{
  if (!msg) {
    return false;
  }
  // is_accelerating
  // is_desclerating
  // joycon_value
  return true;
}

void
ps4_messages__msg__Manette__fini(ps4_messages__msg__Manette * msg)
{
  if (!msg) {
    return;
  }
  // is_accelerating
  // is_desclerating
  // joycon_value
}

bool
ps4_messages__msg__Manette__are_equal(const ps4_messages__msg__Manette * lhs, const ps4_messages__msg__Manette * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // is_accelerating
  if (lhs->is_accelerating != rhs->is_accelerating) {
    return false;
  }
  // is_desclerating
  if (lhs->is_desclerating != rhs->is_desclerating) {
    return false;
  }
  // joycon_value
  if (lhs->joycon_value != rhs->joycon_value) {
    return false;
  }
  return true;
}

bool
ps4_messages__msg__Manette__copy(
  const ps4_messages__msg__Manette * input,
  ps4_messages__msg__Manette * output)
{
  if (!input || !output) {
    return false;
  }
  // is_accelerating
  output->is_accelerating = input->is_accelerating;
  // is_desclerating
  output->is_desclerating = input->is_desclerating;
  // joycon_value
  output->joycon_value = input->joycon_value;
  return true;
}

ps4_messages__msg__Manette *
ps4_messages__msg__Manette__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ps4_messages__msg__Manette * msg = (ps4_messages__msg__Manette *)allocator.allocate(sizeof(ps4_messages__msg__Manette), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ps4_messages__msg__Manette));
  bool success = ps4_messages__msg__Manette__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
ps4_messages__msg__Manette__destroy(ps4_messages__msg__Manette * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    ps4_messages__msg__Manette__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
ps4_messages__msg__Manette__Sequence__init(ps4_messages__msg__Manette__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ps4_messages__msg__Manette * data = NULL;

  if (size) {
    data = (ps4_messages__msg__Manette *)allocator.zero_allocate(size, sizeof(ps4_messages__msg__Manette), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ps4_messages__msg__Manette__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ps4_messages__msg__Manette__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
ps4_messages__msg__Manette__Sequence__fini(ps4_messages__msg__Manette__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      ps4_messages__msg__Manette__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

ps4_messages__msg__Manette__Sequence *
ps4_messages__msg__Manette__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ps4_messages__msg__Manette__Sequence * array = (ps4_messages__msg__Manette__Sequence *)allocator.allocate(sizeof(ps4_messages__msg__Manette__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = ps4_messages__msg__Manette__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
ps4_messages__msg__Manette__Sequence__destroy(ps4_messages__msg__Manette__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    ps4_messages__msg__Manette__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
ps4_messages__msg__Manette__Sequence__are_equal(const ps4_messages__msg__Manette__Sequence * lhs, const ps4_messages__msg__Manette__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!ps4_messages__msg__Manette__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
ps4_messages__msg__Manette__Sequence__copy(
  const ps4_messages__msg__Manette__Sequence * input,
  ps4_messages__msg__Manette__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(ps4_messages__msg__Manette);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    ps4_messages__msg__Manette * data =
      (ps4_messages__msg__Manette *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!ps4_messages__msg__Manette__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          ps4_messages__msg__Manette__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!ps4_messages__msg__Manette__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
