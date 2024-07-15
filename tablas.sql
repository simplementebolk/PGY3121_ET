-- Tabla para RankedAccount
CREATE TABLE ranked_account (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL,
    image VARCHAR(255),
    available BOOLEAN DEFAULT TRUE,
    rank VARCHAR(50) NOT NULL
);

-- Tabla para CartItem
CREATE TABLE cart_item (
    id SERIAL PRIMARY KEY,
    account_id INTEGER REFERENCES ranked_account(id) ON DELETE CASCADE,
    quantity INTEGER DEFAULT 1,
    session_key VARCHAR(40) NOT NULL
);

-- Tabla para ContactForm
CREATE TABLE contact_form (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    rut CHAR(12) NOT NULL,
    dv CHAR(1) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    comuna_id INTEGER REFERENCES comuna(id) ON DELETE CASCADE,
    profesion VARCHAR(100) NOT NULL,
    sexo CHAR(1) NOT NULL CHECK (sexo IN ('M', 'F')),
    ocupacion VARCHAR(100) NOT NULL,
    puesto_empresa VARCHAR(100) NOT NULL
);

-- Tabla para Comuna
CREATE TABLE comuna (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);
