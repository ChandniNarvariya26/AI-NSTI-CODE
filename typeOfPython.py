float1 = 3.14
float2 = -2.718
float3 = 0.0
sum_floats = float1 = float2
product_floats = float1 * 2
difference_floats = float1 - float2
print("\nfloating-point values:")
print("float1 =", float1)
print("float3 =", float3)
print("Sum of floay1 and float2:", sum_floats)
print("product of float1 and 2:", product_floats)
print("difference between float1 and float2:", difference_floats)

complex1 = 2+3j
complex2 = -1-4j
complex3 = 0+0j
sum_complex = complex1 + complex2
product_complex = complex1 * (1+1j)
difference_complex = complex1-complex2
print("\ncomplex values:")
print("complex1=", complex1)
print("complex2=", complex2)
print("complex3=", complex3)
print("sum of complex1 and complex2:", sum_complex)
print("product of complex1 and (1 + 1j):", product_complex)
print("difference between complex1 and complex2:", difference_complex)

single_quoted = 'Hello, World!'
length = len(single_quoted)
upper_case = single_quoted.upper()
lower_case = single_quoted.lower()
contains_substring = 'World' in single_quoted
print("single-quoted string:", single_quoted)
print("Length of the string:", length)
print("Uppercase version:", upper_case)
print("Lowercase version:", lower_case)
print("Contains 'world':", contains_substring)

double_quoted = "Edunrt is awesom"
length = len(double_quoted)
replace_text = double_quoted.replace("awesome", "great")
split_words = double_quoted.split()
print("\nDouble-quoted string:", double_quoted)
print("length of the string:", length)
print("String after replacement:", replace_text)
print("World in the string:", split_words)

int1 = 10
int2 = -5
int3 = 0
print(int1,int2,int3)

float1 = float(int1)
float2 = float(int2)
float3 = float(int3)
print(float1, float2, float3)

string_value = "The number is "
integer_value = 42
integer_as_string = str(integer_value)
result = string_value + integer_as_string
print(result)