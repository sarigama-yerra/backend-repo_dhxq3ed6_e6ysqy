"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Add your own schemas here:
# --------------------------------------------------

class Registration(BaseModel):
    """
    Pendaftaran Ekskul sekolah
    Collection name: "registration"
    """
    student_name: str = Field(..., description="Nama lengkap siswa")
    student_id: str = Field(..., description="NIS / NISN")
    grade: str = Field(..., description="Kelas (contoh: 10)")
    class_name: str = Field(..., description="Rombel (contoh: 10 IPA 2)")
    email: Optional[EmailStr] = Field(None, description="Email siswa")
    phone: str = Field(..., description="No. HP siswa")
    parent_name: Optional[str] = Field(None, description="Nama orang tua / wali")
    parent_phone: Optional[str] = Field(None, description="No. HP orang tua / wali")
    extracurricular: str = Field(..., description="Nama ekskul yang dipilih")
    motivation: Optional[str] = Field(None, description="Alasan / motivasi bergabung")
    experience: Optional[str] = Field(None, description="Pengalaman terkait (opsional)")
    preferred_schedule: Optional[Literal[
        "Senin",
        "Selasa",
        "Rabu",
        "Kamis",
        "Jumat",
        "Sabtu"
    ]] = Field(None, description="Jadwal latihan pilihan")
