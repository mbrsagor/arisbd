def validate_category_data(attrs):
    if "title" in attrs and len(attrs.get("title")) < 1:
        return "category title field is required"
    else:
        return "Please provide valid category title"
