#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
* infinite_while - Enters an infinite loop,
*    pausing for one second in each iteration.
* Return: Always returns 0.
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - code that creates 5 zombie processes
 *
 * Return: Always 0.
 */
int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == 0)
		{
			/*Child process*/
			exit(0);
			/*Child exits immediately, creating a zombie*/
		}
		else if (child_pid > 0)
		{
			/*Parent process*/
			printf("Zombie process created, PID: %d\n", child_pid);
		}
		else
		{
			/*Fork failed*/
			perror("fork");
			exit(1);
		}
	}
	infinite_while();
    /*Keep the parent process running to maintain zombies*/
	return (0);
}


