// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ps4_messages:msg/Manette.idl
// generated code does not contain a copyright notice

#ifndef PS4_MESSAGES__MSG__DETAIL__MANETTE__STRUCT_H_
#define PS4_MESSAGES__MSG__DETAIL__MANETTE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Manette in the package ps4_messages.
typedef struct ps4_messages__msg__Manette
{
  bool is_accelerating;
  bool is_desclerating;
  int32_t joycon_value;
} ps4_messages__msg__Manette;

// Struct for a sequence of ps4_messages__msg__Manette.
typedef struct ps4_messages__msg__Manette__Sequence
{
  ps4_messages__msg__Manette * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ps4_messages__msg__Manette__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PS4_MESSAGES__MSG__DETAIL__MANETTE__STRUCT_H_
