#include <unistd.h>

/**
 * _memset - writes the character c to stdout
 * @s: The character to print
 * @b: character
 * @n: interger
 *
 * Return: On success 1.
 */
char *_memset(char *s, char b, unsigned int n)
{
	char *s_ptr = s;
	while (n > 0)
	{
		*s = b;
		s++;
		n--;
	}
	return s_ptr;
}
