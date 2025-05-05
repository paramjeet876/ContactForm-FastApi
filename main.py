from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr

app = FastAPI()

# Allow requests from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContactForm(BaseModel):
    name: str
    email: EmailStr
    message: str

@app.post("/contact")
async def submit_contact(form: ContactForm):
    # Simulate saving or emailing the contact form data
    print("Received Contact Form:", form.dict())
    return {"message": "Thank you for reaching out, we’ll be in touch soon!"}
