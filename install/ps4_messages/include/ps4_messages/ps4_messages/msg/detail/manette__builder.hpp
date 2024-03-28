// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ps4_messages:msg/Manette.idl
// generated code does not contain a copyright notice

#ifndef PS4_MESSAGES__MSG__DETAIL__MANETTE__BUILDER_HPP_
#define PS4_MESSAGES__MSG__DETAIL__MANETTE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ps4_messages/msg/detail/manette__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ps4_messages
{

namespace msg
{

namespace builder
{

class Init_Manette_joycon_value
{
public:
  explicit Init_Manette_joycon_value(::ps4_messages::msg::Manette & msg)
  : msg_(msg)
  {}
  ::ps4_messages::msg::Manette joycon_value(::ps4_messages::msg::Manette::_joycon_value_type arg)
  {
    msg_.joycon_value = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ps4_messages::msg::Manette msg_;
};

class Init_Manette_is_desclerating
{
public:
  explicit Init_Manette_is_desclerating(::ps4_messages::msg::Manette & msg)
  : msg_(msg)
  {}
  Init_Manette_joycon_value is_desclerating(::ps4_messages::msg::Manette::_is_desclerating_type arg)
  {
    msg_.is_desclerating = std::move(arg);
    return Init_Manette_joycon_value(msg_);
  }

private:
  ::ps4_messages::msg::Manette msg_;
};

class Init_Manette_is_accelerating
{
public:
  Init_Manette_is_accelerating()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Manette_is_desclerating is_accelerating(::ps4_messages::msg::Manette::_is_accelerating_type arg)
  {
    msg_.is_accelerating = std::move(arg);
    return Init_Manette_is_desclerating(msg_);
  }

private:
  ::ps4_messages::msg::Manette msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ps4_messages::msg::Manette>()
{
  return ps4_messages::msg::builder::Init_Manette_is_accelerating();
}

}  // namespace ps4_messages

#endif  // PS4_MESSAGES__MSG__DETAIL__MANETTE__BUILDER_HPP_
