import { useEffect, useState } from "react";
import type { Cliente } from "../../infrastructure/api/clientesApi";
import { listarClientes } from "../../application/usecases/ListarClientes";

export default function ClientesPage() {
  const [clientes, setClientes] = useState<Cliente[]>([]);
  const [error, setError] = useState("");

  useEffect(() => {
    async function cargarClientes() {
      try {
        const data = await listarClientes();
        setClientes(data);
      } catch (err: any) {
        setError(err.response?.data?.detail || err.message || "Error al cargar clientes");
      }
    }

    cargarClientes();
  }, []);

  return (
    <main className="p-6">
      <h1 className="text-2xl font-bold mb-4">Clientes</h1>

      {error && <p className="text-red-600 mb-2">{error}</p>}

      <table className="table-auto border-collapse border border-gray-300 w-full">
        <thead>
          <tr className="bg-gray-200">
            <th className="border p-2">ID</th>
            <th className="border p-2">Nombres</th>
            <th className="border p-2">Apellidos</th>
            <th className="border p-2">Correo</th>
            <th className="border p-2">Teléfono</th>
            <th className="border p-2">Celular</th>
            <th className="border p-2">Dirección</th>
            <th className="border p-2">Saldo</th>
          </tr>
        </thead>
        <tbody>
          {clientes.map(c => (
            <tr key={c.id}>
              <td className="border p-2">{c.id}</td>
              <td className="border p-2">{c.nombres}</td>
              <td className="border p-2">{c.apellidos}</td>
              <td className="border p-2">{c.correo_electronico}</td>
              <td className="border p-2">{c.telefono}</td>
              <td className="border p-2">{c.celular}</td>
              <td className="border p-2">{c.direccion}</td>
              <td className="border p-2">
                {c.saldo.toLocaleString("es-CO", { style: "currency", currency: "COP" })}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </main>
  );
}
