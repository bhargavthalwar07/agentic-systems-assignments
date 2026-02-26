from typing import Optional
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class Address(BaseModel):
    """Address model for user registration."""
    
    city: str = Field(..., min_length=3, description="City name (minimum 3 characters)")
    pincode: str = Field(..., pattern=r"^\d{6}$", description="6-digit pincode")


class User(BaseModel):
    """User model with nested Address and assignment validation."""
    
    model_config = ConfigDict(validate_assignment=True)

    user_id: int = Field(..., description="Unique user identifier")
    name: str = Field(..., description="User's full name")
    email: EmailStr = Field(..., description="Valid email address")
    age: int = Field(..., ge=18, description="User age (must be 18 or older)")
    address: Address = Field(..., description="User's address")
    is_premium: Optional[bool] = Field(default=False, description="Premium membership status")


if __name__ == "__main__":
    # Example: Create a valid user
    address = Address(city="Mumbai", pincode="400001")
    
    user = User(
        user_id=1,
        name="John Doe",
        email="john.doe@example.com",
        age=25,
        address=address
    )
    
    print("User created successfully:")
    print(user.model_dump_json(indent=2))
    
    # Test assignment validation
    print("\nTesting assignment validation...")
    try:
        user.age = 17  # Should raise ValidationError
    except Exception as e:
        print(f"Validation Error: {e}")
    
    # Test invalid pincode
    print("\nTesting invalid pincode...")
    try:
        invalid_address = Address(city="NYC", pincode="12345")  # Not 6 digits
    except Exception as e:
        print(f"Validation Error: {e}")
    
    # Test invalid city length
    print("\nTesting invalid city length...")
    try:
        invalid_address = Address(city="NY", pincode="123456")  # Less than 3 chars
    except Exception as e:
        print(f"Validation Error: {e}")
