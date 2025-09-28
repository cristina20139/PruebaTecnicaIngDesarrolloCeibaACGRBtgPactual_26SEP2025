import axios from "axios";
import type { Fondo } from "../../domain/entidades/Fondo";

const API_URL = "http://localhost:8000/api/fondos";

export async function fetchFondos(): Promise<Fondo[]> {
  const response = await axios.get(API_URL);
  return response.data;
}

export async function crearFondo(fondo: Omit<Fondo, "id">): Promise<Fondo> {
  // Ya no necesitamos mapear, usamos directamente monto_minimo
  const response = await axios.post<Fondo>(API_URL, fondo, {
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
  });
  return response.data;
}
