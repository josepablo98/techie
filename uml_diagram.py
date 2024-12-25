from graphviz import Digraph

# Crear un objeto Digraph para el modelo conceptual UML simplificado
uml = Digraph('Modelo Conceptual', format='png')
uml.attr(rankdir='TB', style='rounded', fontname='Helvetica', bgcolor='#F8F9F9', dpi='300')

# Definir entidades principales simplificadas con atributos completos
uml.node('User', '''<<table border="0" cellborder="1" cellspacing="0">
<tr><td port="header" bgcolor="#AED6F1"><b>User</b></td></tr>
<tr><td align="left">Name</td></tr>
<tr><td align="left">Email</td></tr>
<tr><td align="left">Password</td></tr>
<tr><td align="left">LastPasswordResetRequest</td></tr>
<tr><td align="left">PasswordResetToken</td></tr>
<tr><td align="left">PasswordResetTokenExpires</td></tr>
<tr><td align="left">PasswordResetTokenUsed</td></tr>
<tr><td align="left">PasswordHistory</td></tr>
</table>>''', shape='plaintext', style='rounded')

uml.node('Chat', '''<<table border="0" cellborder="1" cellspacing="0">
<tr><td port="header" bgcolor="#A9DFBF"><b>Chat</b></td></tr>
<tr><td align="left">Date</td></tr>
<tr><td align="left">Messages</td></tr>
</table>>''', shape='plaintext', style='rounded')

uml.node('Settings', '''<<table border="0" cellborder="1" cellspacing="0">
<tr><td port="header" bgcolor="#F9E79F"><b>Settings</b></td></tr>
<tr><td align="left">Theme</td></tr>
<tr><td align="left">Language</td></tr>
<tr><td align="left">DetailLevel</td></tr>
<tr><td align="left">AutoSaveChats</td></tr>
</table>>''', shape='plaintext', style='rounded')

uml.node('Admin', '''<<table border="0" cellborder="1" cellspacing="0">
<tr><td port="header" bgcolor="#F5B7B1"><b>Admin</b></td></tr>
</table>>''', shape='plaintext', style='rounded')

uml.node('Log', '''<<table border="0" cellborder="1" cellspacing="0">
<tr><td port="header" bgcolor="#D7BDE2"><b>Log</b></td></tr>
<tr><td align="left">Date</td></tr>
<tr><td align="left">Type</td></tr>
<tr><td align="left">Description</td></tr>
</table>>''', shape='plaintext', style='rounded')

uml.node('SessionToken', '''<<table border="0" cellborder="1" cellspacing="0">
<tr><td port="header" bgcolor="#FAD7A0"><b>SessionToken</b></td></tr>
<tr><td align="left">Expiration</td></tr>
</table>>''', shape='plaintext', style='rounded')

# Relaciones con cardinalidades y descripciones
uml.edge('User', 'Chat', label='1:N\nCreates chats', color='#2874A6', fontsize='10')
uml.edge('User', 'Settings', label='1:1\nDefines preferences', color='#229954', fontsize='10')
uml.edge('Admin', 'Log', label='1:N\nRecords events', color='#884EA0', fontsize='10')
uml.edge('User', 'SessionToken', label='1:N\nAuthentication', color='#D68910', fontsize='10')
uml.edge('Admin', 'User', label='N:1\nSupervises users', color='#C0392B', fontsize='10')

# Guardar el modelo conceptual simplificado
file_path = 'Modelo Conceptual'
uml.render(file_path)
