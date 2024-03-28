// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ps4_messages:msg/Manette.idl
// generated code does not contain a copyright notice

#ifndef PS4_MESSAGES__MSG__DETAIL__MANETTE__TRAITS_HPP_
#define PS4_MESSAGES__MSG__DETAIL__MANETTE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ps4_messages/msg/detail/manette__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace ps4_messages
{

namespace msg
{

inline void to_flow_style_yaml(
  const Manette & msg,
  std::ostream & out)
{
  out << "{";
  // member: is_accelerating
  {
    out << "is_accelerating: ";
    rosidl_generator_traits::value_to_yaml(msg.is_accelerating, out);
    out << ", ";
  }

  // member: is_desclerating
  {
    out << "is_desclerating: ";
    rosidl_generator_traits::value_to_yaml(msg.is_desclerating, out);
    out << ", ";
  }

  // member: joycon_value
  {
    out << "joycon_value: ";
    rosidl_generator_traits::value_to_yaml(msg.joycon_value, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Manette & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: is_accelerating
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "is_accelerating: ";
    rosidl_generator_traits::value_to_yaml(msg.is_accelerating, out);
    out << "\n";
  }

  // member: is_desclerating
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "is_desclerating: ";
    rosidl_generator_traits::value_to_yaml(msg.is_desclerating, out);
    out << "\n";
  }

  // member: joycon_value
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "joycon_value: ";
    rosidl_generator_traits::value_to_yaml(msg.joycon_value, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Manette & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace ps4_messages

namespace rosidl_generator_traits
{

[[deprecated("use ps4_messages::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ps4_messages::msg::Manette & msg,
  std::ostream & out, size_t indentation = 0)
{
  ps4_messages::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ps4_messages::msg::to_yaml() instead")]]
inline std::string to_yaml(const ps4_messages::msg::Manette & msg)
{
  return ps4_messages::msg::to_yaml(msg);
}

template<>
inline const char * data_type<ps4_messages::msg::Manette>()
{
  return "ps4_messages::msg::Manette";
}

template<>
inline const char * name<ps4_messages::msg::Manette>()
{
  return "ps4_messages/msg/Manette";
}

template<>
struct has_fixed_size<ps4_messages::msg::Manette>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<ps4_messages::msg::Manette>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<ps4_messages::msg::Manette>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PS4_MESSAGES__MSG__DETAIL__MANETTE__TRAITS_HPP_
