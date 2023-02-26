class RandomNumberGenerator {
  late int _value;

  RandomNumberGenerator(int value) {
    _value = value;
  }

// This method generates a new pseudo-random integer using the linear congruential method.
  int nextInt() {
    // define three constants as parameters for the linear congruential method.
    const a = 1103515245;
    const b = 12345;
    const m = 0x7fffffff; // 2^31 - 1
    // use these constants to generate a new pseudo-random integer by multiplying the current value by a, adding b,taking the result modulo m.
    _value = (a * _value + b) % m;
    // update the value value to this new value and return it as the result.
    return _value;
  }

  double nextDouble() {
    const maxInt = 0x7fffffff;
    return nextInt() / (maxInt + 1);
  }
}
