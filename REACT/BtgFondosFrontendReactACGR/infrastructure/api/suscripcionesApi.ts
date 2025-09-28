import axios from "axios";

const API_URL = "http://localhost:8000/api/fondos";

export interface SuscripcionRequest {
  cliente_id: number;
  monto: number;
}

export interface Suscripcion {
  cliente_id: number;
  fondo_id: number;
  monto: number;
  tipo: string;
  fecha: string;
}

export async function suscribirse(fondo_id: number, data: SuscripcionRequest): Promise<Suscripcion> {
  const response = await axios.post<Suscripcion>(`${API_URL}/${fondo_id}/suscribirse`, data, {
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
  });
  return response.data;
}
