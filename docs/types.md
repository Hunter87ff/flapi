## Types

Data Types are the types which you have to define in the schema. For example, `name()`. Make sure that it ends with `()`.

Currently, there are various kinds of types available.

### name()
`name()` is a static type that returns a name of an individual.

**Parameters**:
- `len`: Refers to the length of the name. Minimum is 5.

**Return Type**:
- Returns a `string` type of data.

### email()
`email()` is a static type that returns an email address.

**Parameters**:
- `domain`: Specifies the domain of the email. For example, `domain=hg.co`.

**Return Type**:
- Returns a `string` type of data.

### age()
`age()` is a static type that returns an age.

**Parameters**:
- `min`: Specifies the minimum age. For example, `min=78`.
- `max`: Specifies the maximum age. For example, `max=200`.

**Return Type**:
- Returns an `integer` type of data.

### address()
`address()` is a static type that returns an address.

**Parameters**:
- None.

**Return Type**:
- Returns a `string` type of data.

### date()
`date()` is a static type that returns a date.

**Parameters**:
- None.

**Return Type**:
- Returns a `date` type of data.

### phone()
`phone()` is a static type that returns a phone number.

**Parameters**:
- `code`: Specifies the country code of the phone number. For example, `code=87`.

**Return Type**:
- Returns a `string` type of data.

### list-str()
`list-str()` is a static type that returns a list of strings.

**Parameters**:
- `amount`: Specifies the number of strings in the list. For example, `amount=3`.

**Return Type**:
- Returns a `list` of `string` type data.
