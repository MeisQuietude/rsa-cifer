import os
import rsa


def create_keys(strength = 1024):
    (public, private) = rsa.newkeys(strength)

    print('Strength:', strength)

    os.mkdir('.rsa')
    with open ('.rsa/key', 'w') as f:
        f.write(str(private))
    print('[+] key Created Successfully')

    with open('.rsa/key.pub', 'w') as f:
        f.write(str(public))
    print('[+] key.pub Created Successfully')

    print('\nPublic key:')
    print(public)


if __name__ == '__main__':
    create_keys()