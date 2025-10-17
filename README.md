Medly backend API running on Docker

## Data Model

```sql
-- =======================
-- Users
-- =======================
CREATE TABLE users (
    user_id VARCHAR(50) PRIMARY KEY,
    display_name VARCHAR(255),
    email VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_seen TIMESTAMP,
    metadata JSONB
);

-- =======================
-- Curriculum: Units → Topics → Lessons
-- =======================
CREATE TABLE units (
    unit_id SERIAL PRIMARY KEY,
    unit_index INT NOT NULL,
    unit_title VARCHAR(255) NOT NULL
);

CREATE TABLE topics (
    topic_id SERIAL PRIMARY KEY,
    unit_id INT NOT NULL REFERENCES units(unit_id),
    topic_index INT NOT NULL,
    topic_title VARCHAR(255) NOT NULL
);

CREATE TABLE lessons (
    lesson_id VARCHAR(50) PRIMARY KEY,  -- stable lessonID from course JSON
    topic_id INT NOT NULL REFERENCES topics(topic_id),
    lesson_index INT NOT NULL,
    lesson_title VARCHAR(255) NOT NULL
);

CREATE TABLE lesson_chunks (
    chunk_id SERIAL PRIMARY KEY,
    lesson_id VARCHAR(50) NOT NULL REFERENCES lessons(lesson_id),
    chunk_index INT NOT NULL,
    chunk_title VARCHAR(255) NOT NULL
);

-- =======================
-- Assessments
-- =======================
CREATE TABLE papers (
    paper_id VARCHAR(50) PRIMARY KEY,
    board VARCHAR(50),
    qualification VARCHAR(50),
    subject VARCHAR(50),
    series VARCHAR(50),
    tier VARCHAR(50)
);

CREATE TABLE practice_items (
    question_id VARCHAR(50) PRIMARY KEY,
    lesson_id VARCHAR(50) REFERENCES lessons(lesson_id),
    question_text TEXT,
    question_part INT,
    markscheme TEXT,
    markmax INT,
    difficulty INT,
    specification_point TEXT,
    options JSONB,
    correct_answer_index JSONB,
    question_diagram JSONB,
    source_file VARCHAR(255),
    first_seen TIMESTAMP,
    last_seen TIMESTAMP
);

CREATE TABLE paper_questions (
    paper_id VARCHAR(50) REFERENCES papers(paper_id),
    question_id VARCHAR(50),
    PRIMARY KEY (paper_id, question_id)
);

-- =======================
-- User Question Attempts
-- =======================
CREATE TABLE user_question_attempts (
    user_id VARCHAR(50) REFERENCES users(user_id),
    question_id VARCHAR(50) REFERENCES practice_items(question_id),
    is_marked BOOLEAN NOT NULL,
    user_answer TEXT,
    annotated_answer TEXT,
    user_mark INT,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP,
    metadata JSONB,
    PRIMARY KEY (user_id, question_id)
);
```