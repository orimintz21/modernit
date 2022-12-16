import number_theory_functions


class RSA():
    def __init__(self,  public_key, private_key=None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate(digits=10):
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """
        q = number_theory_functions.generate_prime(digits)
        p = number_theory_functions.generate_prime(digits)
        while p == q:
            p = number_theory_functions.generate_prime(digits)
        N = p * q
        K = (p - 1) * (q - 1)
        """ we chose e = 65537 """
        e = 65537
        d = number_theory_functions.modular_inverse(e, K)

        return RSA((N, e), (N, d))

    def encrypt(self, m):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        return number_theory_functions.modular_exponent(m, self.public_key[1], self.public_key[0])

    def decrypt(self, c):
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
        """
        return number_theory_functions.modular_exponent(c, self.private_key[1], self.private_key[0])
