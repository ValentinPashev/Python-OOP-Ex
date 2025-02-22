def math_operations(*numbers, **kwargs):
    keys = list(kwargs.keys())

    for i in range(len(numbers)):
        key = keys[i % 4]

        if key == "a":
            kwargs[key] += numbers[i]

        elif key == "s":
            kwargs[key] -= numbers[i]

        elif key == "d":
            if numbers[i] != 0:
                kwargs[key] /= numbers[i]

        elif key == "m":
            kwargs[key] *= numbers[i]

    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    return "\n".join(f"{key}: {value:.1f}" for key, value in kwargs)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
