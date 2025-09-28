import axios from "axios";

export interface Cliente {
  id: number;
  nombres: string;
  apellidos: string;
  correo_electronico: string;
  telefono: string;
  celular: string;
  direccion: string;
  saldo: number;
}

const API_URL = "http://localhost:8000/api/clientes";

export async function fetchClientes(): Promise<Cliente[]> {
  const response = await axios.get<Cliente[]>(API_URL, {
    headers: {
      Accept: "application/json",
    },
  });
  return response.data;
}
