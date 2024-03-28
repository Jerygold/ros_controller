// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ps4_messages:msg/Manette.idl
// generated code does not contain a copyright notice

#ifndef PS4_MESSAGES__MSG__DETAIL__MANETTE__STRUCT_HPP_
#define PS4_MESSAGES__MSG__DETAIL__MANETTE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__ps4_messages__msg__Manette __attribute__((deprecated))
#else
# define DEPRECATED__ps4_messages__msg__Manette __declspec(deprecated)
#endif

namespace ps4_messages
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Manette_
{
  using Type = Manette_<ContainerAllocator>;

  explicit Manette_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_accelerating = false;
      this->is_desclerating = false;
      this->joycon_value = 0l;
    }
  }

  explicit Manette_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_accelerating = false;
      this->is_desclerating = false;
      this->joycon_value = 0l;
    }
  }

  // field types and members
  using _is_accelerating_type =
    bool;
  _is_accelerating_type is_accelerating;
  using _is_desclerating_type =
    bool;
  _is_desclerating_type is_desclerating;
  using _joycon_value_type =
    int32_t;
  _joycon_value_type joycon_value;

  // setters for named parameter idiom
  Type & set__is_accelerating(
    const bool & _arg)
  {
    this->is_accelerating = _arg;
    return *this;
  }
  Type & set__is_desclerating(
    const bool & _arg)
  {
    this->is_desclerating = _arg;
    return *this;
  }
  Type & set__joycon_value(
    const int32_t & _arg)
  {
    this->joycon_value = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ps4_messages::msg::Manette_<ContainerAllocator> *;
  using ConstRawPtr =
    const ps4_messages::msg::Manette_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ps4_messages::msg::Manette_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ps4_messages::msg::Manette_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ps4_messages::msg::Manette_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ps4_messages::msg::Manette_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ps4_messages::msg::Manette_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ps4_messages::msg::Manette_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ps4_messages::msg::Manette_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ps4_messages::msg::Manette_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ps4_messages__msg__Manette
    std::shared_ptr<ps4_messages::msg::Manette_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ps4_messages__msg__Manette
    std::shared_ptr<ps4_messages::msg::Manette_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Manette_ & other) const
  {
    if (this->is_accelerating != other.is_accelerating) {
      return false;
    }
    if (this->is_desclerating != other.is_desclerating) {
      return false;
    }
    if (this->joycon_value != other.joycon_value) {
      return false;
    }
    return true;
  }
  bool operator!=(const Manette_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Manette_

// alias to use template instance with default allocator
using Manette =
  ps4_messages::msg::Manette_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ps4_messages

#endif  // PS4_MESSAGES__MSG__DETAIL__MANETTE__STRUCT_HPP_
