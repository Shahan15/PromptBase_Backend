# 🧠 PromptBase — AI Prompt Refinement (Backend)

This is the **Backend API** for PromptBase, a full-stack platform for optimizing and managing AI prompts. It handles logic for prompt refinement via Google Gemini, data persistence via Supabase, and secure JWT-based authentication.

### 🔗 Frontend Repository
The React-based frontend for this project is located here:
👉 **[PromptBase Frontend](https://github.com/Shahan15/PromptBase_FrontEnd)**

---

## 🚀 Features

### ✨ Prompt Tools
* **AI Optimization:** Refine raw prompts into high-quality inputs using Google Gemini.
* **Management:** Full CRUD (Create, Read, Update, Delete) for prompt storage.
* **Favorites:** Quick-save high-performing prompts to a dedicated list.

### 👤 User Accounts
* **Supabase Auth:** Secure user registration and login.
* **JWT Security:** Route protection using `PyJWT` and `passlib`.
* **Isolated Data:** Database Row Level Security (RLS) ensures users only access their own prompts.

---

## 🗂️ Database Schema

Before running the backend, you must set up the following tables in your Supabase project.


### 1. Schema Overview
* **`users`**: Managed primarily by Supabase Auth, but extended with custom fields like `first_name` and `last_name`.
* **`prompts`**: Stores the `original_prompt`, the Gemini-generated `optimised_prompt`, and a `user_id` foreign key.
* **`favourites`**: A join table linking `user_id` to `prompt_id` for quick filtering.

### 2. SQL Setup Script
Copy and paste this into your **Supabase SQL Editor** to create the necessary tables:

```sql
-- Create Users Table (Extended profile)
CREATE TABLE users (
  id UUID REFERENCES auth.users ON DELETE CASCADE PRIMARY KEY,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  first_name TEXT,
  last_name TEXT,
  email TEXT UNIQUE,
  password TEXT -- Stored as a hashed string
);

-- Create Prompts Table
CREATE TABLE prompts (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  original_prompt TEXT NOT NULL,
  optimised_prompt TEXT,
  is_private BOOLEAN DEFAULT TRUE,
  tags TEXT, -- Comma-separated strings
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE
);

-- Create Favourites Table
CREATE TABLE favourites (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  prompt_id UUID REFERENCES prompts(id) ON DELETE CASCADE,
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE
);
```



## 🛠️ Installation & Setup

### 3. Clone & Environment
```bash
git clone https://github.com/Shahan15/PromptBase_Backend.git
cd PromptBase_Backend
python3 -m venv venv
source venv/bin/activate

```

##  Install Dependencies

This project requires **specific version pinning** to resolve compatibility issues between `passlib` and newer `bcrypt` versions on macOS.

### Install FastAPI (required for `fastapi dev`)
```bash
pip install "fastapi[standard]"
```

### Install Database & AI SDKs
```bash
pip install supabase python-dotenv pydantic-settings google-genai
```

### Critical: Pin bcrypt for passlib compatibility
```bash
pip install "passlib[bcrypt]" bcrypt==4.0.1
```
## 4. Environment Variables
Create a .env file in the root directory:
```env
Code snippet

SUPABASE_URL=[https://zeenbazlfhshamwqmifu.supabase.co](https://zeenbazlfhshamwqmifu.supabase.co)
SUPABASE_KEY=your_service_role_key
GEMINI_API_KEY=your_gemini_api_key
JWT_SECRET=your_secure_hex_string
JWT_ALGORITHM=HS256
JWT_EXPIRES_IN=30
```

## 🚦 Running the Application
To ensure the app module is recognised correctly by the Python path, run the server from the root directory using:

Development Mode (Auto-reload):

```bash

PYTHONPATH=. fastapi dev app/main.py
```

### Production Mode
```bash
PYTHONPATH=. fastapi run app/main.py
```
## 💡 Troubleshooting (Mac/zsh)

If you encounter issues during setup, check these common fixes for macOS users:

> **Package Installation:** If you see `zsh: no matches found: fastapi[standard]`, ensure you wrap the package name in double quotes:  
> `pip install "fastapi[standard]"`

* **ModuleNotFoundError: No module named 'app'** You must run the server command from the root folder (`PromptBase_Backend`) and include the `PYTHONPATH=.` prefix so Python can locate your local modules.

* **AttributeError: module 'google.generativeai' has no attribute 'Client'** This project uses the newer `google-genai` SDK. Ensure you have installed `google-genai` and **not** the older `google-generativeai` package.

---

## 📦 Roadmap

- [ ] **Prompt Search:** Add server-side search and filtering capabilities.
- [ ] **Version History:** Implement a "history" feature to track prompt iterations.
- [ ] **Categorization:** Add tags and custom categories for better management.
- [ ] **Production Deployment:** Configure Docker and deploy to Render or Fly.io.

