export interface Macros {
    calorias: number; 
    proteinas: number; 
    carbohidratos: number; 
    grasas: number; 
}

export interface PerfilUsuario {
    id: number; 
    username: string; 
    fecha_nacimiento: string | null; 
    peso: number | null; 
    altura: number | null; 
    sexo: string | null; 
    nivel_actividad: string | null; 
}

export interface ObjetivoUsuario extends Macros {
    id: number; 
    nombre: string; 
    marca?: string | null; 
}

export interface Alimento extends Macros {
    id: number; 
    nombre: string; 
    marca? : string | null; 
}

export interface AlimentoConsumido {
    id: number; 
    registro: number; 
    alimento: number; 
    alimento_nombre? : string;
    cantidad_gramos: number; 
    macros_calculados: Macros;
}

export interface RegistroComida {
    id:number; 
    fecha: string; 
    comida: string; 
    alimentos_consumidos: AlimentoConsumido[]; 
    totales_comida: Macros;
}

export interface AuthTokens {
    access: string; 
    refresh: string;
}