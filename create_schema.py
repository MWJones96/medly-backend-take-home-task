import json
from genson import SchemaBuilder

def main():
    input = [
        'user_data/user_data.json', 
        'curriculum_data/aqaGCSEBio_course.json', 
        'curriculum_data/aqaGCSEBio_exams.json', 
        'curriculum_data/aqaGCSEBio_practices.json'
    ]
    output = [
        'user_data/user_data_schema.json', 
        'curriculum_data/aqaGCSEBio_course_schema.json', 
        'curriculum_data/aqaGCSEBio_exams_schema.json', 
        'curriculum_data/aqaGCSEBio_practices_schema.json'
    ]
    
    io = zip(input, output)
    input, output = next(io)
    builder = SchemaBuilder()

    with open(input, "r") as f:
        data = json.load(f)
        
        for k, v in data["targets"].items():
            user_id = k.split('/')[1]
            v["userID"] = user_id
            builder.add_object(v)
    
    with open(output, "w") as f:
        f.write(json.dumps(builder.to_schema(), indent=2))
        
    for i, o in io:
        builder = SchemaBuilder()
        with open(i, "r") as f:
            data = json.load(f)
            builder.add_object(data)
        
        with open(o, "w") as f:
            f.write(json.dumps(builder.to_schema(), indent=2))

if __name__ == "__main__":
    main()