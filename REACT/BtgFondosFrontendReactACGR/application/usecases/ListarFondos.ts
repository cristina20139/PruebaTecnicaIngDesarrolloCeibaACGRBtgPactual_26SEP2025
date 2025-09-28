import { fetchFondos } from "../../infrastructure/api/fondosApi";
import type { Fondo } from "../../domain/entidades/Fondo";

export async function listarFondos(): Promise<Fondo[]> {
  return await fetchFondos();
}
