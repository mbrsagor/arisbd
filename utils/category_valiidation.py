def validate_category_data(attrs):
    if "category_name" in attrs and len(attrs.get("category_name")) < 1:
        return "category field is required"
    else:
        return "Please provide valid category name"
