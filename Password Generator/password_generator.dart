import 'dart:math';

// the code uses Dart's built-in Random class to generate a random password by selecting characters from a set of lowercase letters,
// uppercase letters, digits, and symbols. It then prints the password to the console.

void main() {
  // character for generating the password
  final lowerChars = 'abcdefghijklmnopqrstuvwxyz';
  final upperChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  final digitChars = '0123456789';
  final symbolChars = '!@#\$%^&*()-_=+[]{}|;:,.<>?';

  // Combine the character sets into a single string
  final allChars = lowerChars + upperChars + digitChars + symbolChars;

  // length of the password to generate
  final passwordLength = 12;

  // Generate the password
  final random = Random.secure();
  final password = String.fromCharCodes(
    Iterable.generate(
      passwordLength,
      (_) => allChars.codeUnitAt(
        random.nextInt(allChars.length),
      ),
    ),
  );

  // Print the generated password 
  print(password);
}
