##############################################################################
#
# Constants - Laptop specifications that the user can answer

LAPTOP_SPECIFICATIONS = [
'Operating System (e.g. Windows 10, Mac)', 
'Price / Price Range (e.g. $799, $500 - $1000)', 
'Brand (e.g. Dell, Lenovo)', 
'Screen Size (e.g. 14", 15.6")', 
'RAM (e.g. 6GB, 8GB)', 
'Processor Brand (e.g. Intel, AMD)', 
'Processor Model (e.g. Intel i5, AMD A6)', 
'Features (e.g. Touch Screen, 2-in-1)', 
'Condition (e.g. New, Refurbished)',
'Other (e.g. Storage Type, Screen Resolution, Color, etc.)']

##############################################################################
#
# Public Functions

def get_laptop_specs()->list:
 	"""
 	Gets the user's desired specifications, 
 	handles empty and multiple inputs (e.g. "" or "6GB RAM, 8GB RAM"), 
 	and returns them in a list
 	"""
 	print("Enter desired specifctions (leave blank if specification does not matter)")
 	user_specs = [str(input("{}: ".format(spec))) for spec in LAPTOP_SPECIFICATIONS]
 	user_specs = _empty_inputs(user_specs)
 	user_specs = _multiple_inputs(user_specs)
 	return user_specs

##############################################################################
#
# Private Functions

def _empty_inputs(specs:list)->list:
	"""
	Gets rid of empty inputs in specs
	"""
	return [spec for spec in specs if spec != ""]

def _multiple_inputs(specs:list)->list:
	"""
	Turns inputs with multiple specs into a list
	"""
	return [spec.split(",") if "," in spec else spec for spec in specs]