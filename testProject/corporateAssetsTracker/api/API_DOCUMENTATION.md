## Company

### List Companies

Returns a list of all the companies.

```
GET  http://127.0.0.1:8000/api/v1/companies/
```

#### Response

```
[
    {
        "id": 1,
        "name": "ACME Corporation"
    },
    {
        "id": 2,
        "name": "Globex Corporation"
    }
]

```

## Create Company

### Creates a new company

```
POST  http://127.0.0.1:8000/api/v1/companies/
```

#### Request Body

```
{
    "name": "ACME Corporation"
}
```

#### Response

```
{
    "id": 1,
    "name": "ACME Corporation"
}
```

#### Get Company By Id

```
GET  http://127.0.0.1:8000/api/v1/companies/1
```

#### Response

```
    {
        "id": 1,
        "name": "ACME Corporation"
    }
```

## Employee

### List Employees

#### Returns a list of all the employees.

```
GET  http://127.0.0.1:8000/api/v1/emplyees/
```

#### Response

```
[
    {
        "id": 1,
        "name": "John Smith",
        "company": {
            "id": 1,
            "name": "ACME Corporation"
        }
    },
    {
        "id": 2,
        "name": "Jane Doe",
        "company": {
            "id": 1,
            "name": "ACME Corporation"
        }
    }
]
```

## Create Employee

### Creates a new employee.

```
POST  http://127.0.0.1:8000/api/v1/emplyees/
```

#### Request Body

```
{
    "name": "John Smith",
    "company": 1
}
```

#### Response

```
{
    "id": 1,
    "name": "John Smith",
    "company": {
        "id": 1,
        "name": "ACME Corporation"
    }
}
```

#### Get Employee By Id

```
GET  http://127.0.0.1:8000/api/v1/employee/1
```

#### Response

```
    {
    "id": 1,
    "name": "John Smith",
    "company": {
        "id": 1,
        "name": "ACME Corporation"
    }
}
```

## Device

### List Devices

#### Returns a list of all the devices.

```
GET  http://127.0.0.1:8000/api/v1/devices/
```

#### Response

```
[
    {
        "id": 1,
        "name": "Macbook Pro",
        "company": {
            "id": 1,
            "name": "ACME Corporation"
        },
        "description": "A laptop"
    },
    {
        "id": 2,
        "name": "iPhone 12",
        "company": {
            "id": 1,
            "name": "ACME Corporation"
        },
        "description": "A phone"
    }
]
```

## Create Device

### Creates a new device.

```
POST  http://127.0.0.1:8000/api/v1/devices/
```

#### Request Body

```
{
    "name": "Macbook Pro",
    "company": 1,
    "description": "A laptop"
}
```

#### Response

```
{
    "id": 1,
    "name": "Macbook Pro",
    "company": {
        "id": 1,
        "name": "ACME Corporation"
    },
    "description": "A laptop"
}
```

#### Get Devices By Id

```
GET  http://127.0.0.1:8000/api/v1/devices/1
```

#### Response

```
{
    "id": 1,
    "employee": {
        "id": 1,
        "name": "John Smith",
        "company": {
            "id": 1,
            "name": "ACME Corporation"
        }
    },
}
```

## DeviceLog

### List Device Logs

#### Returns a list of all the device logs.

```
GET  http://127.0.0.1:8000/api/v1/devicelogs/
```

#### Response

```
[
    {
        "id": 1,
        "employee": {
            "id": 1,
            "name": "John Smith",
            "company": {
                "id": 1,
                "name": "ACME Corporation"
            }
        },
        "device": {
            "id": 1,
            "name": "Macbook Pro",
            "company": {
                "id": 1,
                "name": "ACME Corporation"
            },
            "description": "A
    }
]
```

#### Get DeviceLog By Id

```
GET  http://127.0.0.1:8000/api/v1/devicelogs/1
```

#### Response

```
{
    "id": 1,
    "employee": {
        "id": 1,
        "name": "John Smith",
        "company": {
            "id": 1,
            "name": "ACME Corporation"
        }
    },
}
```
