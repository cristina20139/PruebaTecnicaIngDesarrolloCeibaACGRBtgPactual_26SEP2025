import type { Fondo } from "../../domain/entidades/Fondo";
import { crearFondo } from "../../infrastructure/api/fondosApi";

export async function registrarFondo(fondo: Omit<Fondo, "id">): Promise<Fondo> {
  return await crearFondo(fondo);
}
