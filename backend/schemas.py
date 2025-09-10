from pydantic import BaseModel, Field, field_validator

class PromptRequest(BaseModel):
    prompt: str = Field(...,
                        min_length=10,
                        max_length=500,
                        example="Write a romantic poem on eyes" , 
                        description="The text prompt to generate a response for"
                    )

    @field_validator('prompt')
    def validate_prompt(value):
        if not value.strip():
            raise ValueError("Prompt cannot be empty")
        elif len(value) < 10:
            raise ValueError("Prompt must be at least 10 characters long")
        elif len(value) > 500:
            raise ValueError("Prompt cannot exceed 500 characters")
        return value

class GeneratedText(BaseModel):
    generated_text: str = Field(..., example= "Your eyes are as beautiful as moon",description="The generated text response based on the prompt")
    
    @field_validator('generated_text')
    def validate_text(value):
        if not value.strip():
            raise ValueError("Generated text cannot be empty")
        return value