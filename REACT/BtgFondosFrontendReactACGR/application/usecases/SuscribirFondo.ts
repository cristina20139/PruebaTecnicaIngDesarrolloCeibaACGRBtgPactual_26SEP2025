import type { Suscripcion, SuscripcionRequest } from "../../infrastructure/api/suscripcionesApi";
import { suscribirse } from "../../infrastructure/api/suscripcionesApi";

export async function registrarSuscripcion(fondo_id: number, data: SuscripcionRequest): Promise<Suscripcion> {
  return await suscribirse(fondo_id, data);
}
