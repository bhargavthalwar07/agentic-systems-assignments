from pydantic import BaseModel, EmailStr, Field, ValidationError


class UserRegister(BaseModel):
    """User registration model with validation."""
    
    username: str = Field(..., min_length=5, description="Username (minimum 5 characters)")
    email: EmailStr = Field(..., description="Valid email address")
    age: int = Field(..., ge=18, description="Age (must be 18 or older)")


if __name__ == "__main__":
    # Valid user registration
    print("--- Valid User Registration ---")
    try:
        user = UserRegister(
            username="johndoe",
            email="john@example.com",
            age=25
        )
        print(f"Registration successful: {user.model_dump()}")
    except ValidationError as e:
        print(f"Validation Error: {e}")

    # Invalid: username too short
    print("\n--- Invalid: Username too short ---")
    try:
        user = UserRegister(
            username="john",
            email="john@example.com",
            age=25
        )
    except ValidationError as e:
        print(f"Validation Error: {e}")

    # Invalid: invalid email
    print("\n--- Invalid: Invalid email ---")
    try:
        user = UserRegister(
            username="johndoe",
            email="invalid-email",
            age=25
        )
    except ValidationError as e:
        print(f"Validation Error: {e}")

    # Invalid: age less than 18
    print("\n--- Invalid: Age less than 18 ---")
    try:
        user = UserRegister(
            username="johndoe",
            email="john@example.com",
            age=16
        )
    except ValidationError as e:
        print(f"Validation Error: {e}")
