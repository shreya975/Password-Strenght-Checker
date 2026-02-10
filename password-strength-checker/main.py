from src.validator import validate_password

def main():
    password = input("Enter your password: ")
    result = validate_password(password)

    print("\nValidation Result:")
    for rule, passed in result.items():
        status = "PASS" if passed else "FAIL"
        print(f"{rule:<10} : {status}")

if __name__ == "__main__":
    main()
