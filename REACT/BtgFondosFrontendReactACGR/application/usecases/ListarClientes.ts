import type { Cliente } from "../../infrastructure/api/clientesApi";
import { fetchClientes } from "../../infrastructure/api/clientesApi";

export async function listarClientes(): Promise<Cliente[]> {
  return await fetchClientes();
}
