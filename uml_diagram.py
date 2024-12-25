from graphviz import Digraph

# Crear un objeto Digraph para el modelo conceptual UML
uml = Digraph('Modelo Conceptual', format='png')
uml.attr(rankdir='TB', style='rounded', fontname='Helvetica', bgcolor='#F8F9F9', dpi='300')

# Definir entidades principales con atributos en filas
uml.node('User', '''{User|
- ID: INT (PK) \\l
- Name: VARCHAR(255) \\l
- Email: VARCHAR(255) (UNIQUE) \\l
- Password: VARCHAR(255) \\l
- LastPasswordResetRequest: DATETIME \\l
- PasswordResetToken: VARCHAR(255) \\l
- PasswordResetTokenExpires: DATETIME \\l
- PasswordResetTokenUsed: BOOLEAN \\l
- PasswordHistory: JSON \\l}''', shape='record', style='filled', fillcolor='#AED6F1')

uml.node('Chat', '''{Chat|
- ID: INT (PK) \\l
- UserID: INT (FK) \\l
- Date: DATETIME \\l
- Messages: JSON \\l}''', shape='record', style='filled', fillcolor='#A9DFBF')

uml.node('Settings', '''{Settings|
- ID: INT (PK) \\l
- UserID: INT (FK) \\l
- Theme: VARCHAR(50) \\l
- Language: VARCHAR(50) \\l
- DetailLevel: VARCHAR(50) \\l
- AutoSaveChats: BOOLEAN \\l}''', shape='record', style='filled', fillcolor='#F9E79F')

uml.node('Admin', '''{Admin|
- ID: INT (PK) \\l
- UserID: INT (FK) \\l}''', shape='record', style='filled', fillcolor='#F5B7B1')

uml.node('Log', '''{Log|
- ID: INT (PK) \\l
- AdminID: INT (FK) \\l
- Date: DATETIME \\l
- Type: VARCHAR(255) \\l
- Description: TEXT \\l}''', shape='record', style='filled', fillcolor='#D7BDE2')

uml.node('SessionToken', '''{SessionToken|
- ID: INT (PK) \\l
- UserID: INT (FK) \\l
- Expiration: DATETIME \\l}''', shape='record', style='filled', fillcolor='#FAD7A0')

# Relaciones con más detalles y cardinalidades
uml.edge('User', 'Chat', label='1:N\nCreates chats', color='#2874A6', fontsize='10')
uml.edge('User', 'Settings', label='1:1\nDefines preferences', color='#229954', fontsize='10')
uml.edge('Admin', 'Log', label='1:N\nRecords events', color='#884EA0', fontsize='10')
uml.edge('User', 'SessionToken', label='1:N\nAuthentication', color='#D68910', fontsize='10')
uml.edge('Admin', 'User', label='N:1\nSupervises users', color='#C0392B', fontsize='10')

# Subgrupos para alineación
with uml.subgraph() as s:
    s.attr(rank='same')  # Alinear las entidades secundarias en el mismo nivel
    s.node('Chat')
    s.node('Settings')
    s.node('SessionToken')
    s.node('Log')

# Guardar el modelo conceptual
file_path = 'Modelo Conceptual'
uml.render(file_path)
