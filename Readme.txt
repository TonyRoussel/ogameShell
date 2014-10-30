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

From here, order can be sended to the session
username@universe > build planet_name 250 turrets

To log on another account just use the log command as explain.
To choose which one you focus just type:
username@universe > focus username@universe2
