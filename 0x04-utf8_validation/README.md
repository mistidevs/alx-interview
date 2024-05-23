# UTF8 Validation
## Method
Using bitwise operations to check if the number encodings are valid 1 to 4 byte representations of UTF8 characters. Moreover, for multibyte characters continuation characters are validated.

If there is any failure at any point then the data set is not a valid UTF8 compliant data set.
