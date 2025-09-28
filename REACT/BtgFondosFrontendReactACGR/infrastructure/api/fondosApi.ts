import axios from "axios";
import type { Fondo } from "../../domain/entidades/Fondo";


const API_URL = "http://localhost:8000/api/fondos";

export async function fetchFondos(): Promise<Fondo[]> {
  const response = await axios.get(API_URL);
  return response.data;
}
