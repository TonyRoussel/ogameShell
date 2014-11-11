This is a training project, so I apologise if some lines doesn't stick to the pythonic good practice :)

The purpose of ogmShell is to provide a simple command-line based interface to ogame.
Further extensions will provide more complex queue order and multi-account interaction.

When launch, ogmShell's prompt only display a simple bracket waiting for command:
>

To log an account, one need to type the following:
> log universe username

Unless the asked universe doesn't exist or is doesn't supported yet, the user is ask for a password:
> log universe username
Password: 

On success, the ogame session is added to the SessionManagingList and the new session is focus
username@universe >

To log on another account just use the log command as explain.
To choose which one you focus just type:
username@universe > focus username@universe2

Or simply use the 'switch' command to switch between the sessions

From here, order can be sended to the session
username@universe > build planet_name 250 turrets (currently in dev)


___________________________________________


Commands list

'get' command: (currently in dev)
The intend of 'get' command is to provide a easy way to retrieve intel on an account.
Without any arguments, it displays general information about the focused session, such as the under attack
status, the pending messages, the current friendly missions in progress, and summed resources and ships
on all planets.
Provided options can be used to filter intels:
		 -h display this help
		 -U under attack status
		 -m pending messages
		 -S ships quantity
		 -R display resources status
		 -p display informations planet by planet (no sum)
		 
