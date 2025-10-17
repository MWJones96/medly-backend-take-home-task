Medly backend API running on Docker

# Stage 1: Data Normalisation

## Raw Data

### Users
| Column           | Type      | Nullable | Notes         |
| ---------------- | --------- | -------- | ------------- |
| id               | SERIAL    | NO       | Primary Key   |
| user_id          | VARCHAR   | NO       | Required      |
| question_id      | VARCHAR   | NO       | Required      |
| created_at       | TIMESTAMP | NO       | Required      |
| is_marked        | BOOLEAN   | NO       | Required      |
| user_mark        | INTEGER   | YES      | Optional      |
| annotated_answer | TEXT      | YES      | Optional      |
| user_answer      | TEXT      | YES      | Optional      |
| marking_table    | TEXT      | YES      | Optional      |
| updated_at       | TIMESTAMP | YES      | Optional      |

### Units
| Column     | Type    | Nullable | Notes                |
| ---------- | ------- | -------- | -------------------- |
| unit_index | INTEGER | NO       | Part of composite PK |
| unit_title | TEXT    | NO       | Required             |

### Topics
| Column      | Type    | Nullable | Notes                  |
| ----------- | ------- | -------- | ---------------------- |
| unit_index  | INTEGER | NO       | FK → units(unit_index) |
| topic_index | INTEGER | NO       | Part of composite PK   |
| topic_title | TEXT    | NO       | Required               |

### Lessons
| Column       | Type    | Nullable | Notes                                |
| ------------ | ------- | -------- | ------------------------------------ |
| unit_index   | INTEGER | NO       | FK → units(unit_index)               |
| topic_index  | INTEGER | NO       | FK → topics(unit_index, topic_index) |
| lesson_index | INTEGER | NO       | Part of composite PK                 |
| lesson_id    | TEXT    | NO       | Required                             |
| lesson_title | TEXT    | NO       | Required                             |
