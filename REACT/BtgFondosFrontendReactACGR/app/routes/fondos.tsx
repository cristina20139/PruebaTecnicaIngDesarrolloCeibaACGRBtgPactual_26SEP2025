// app/routes/fondos.tsx
import { useEffect, useState } from "react";
import type { Fondo } from "../domain/entidades/Fondo"; // 👈 importa el tipo
import axios from "axios";

export default function FondosPage() {
  const [fondos, setFondos] = useState<Fondo[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get<Fondo[]>("http://localhost:8000/api/fondos")
      .then((response) => {
        setFondos(response.data);
      })
      .catch((error) => {
        console.error("Error al cargar fondos:", error);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  return (
    <main className="flex flex-col items-center p-6">
      <h1 className="text-2xl font-bold mb-6">Listado de Fondos</h1>

      {loading ? (
        <p>Cargando...</p>
      ) : (
        <table className="table-auto border-collapse border border-gray-300 dark:border-gray-700">
          <thead>
            <tr className="bg-gray-100 dark:bg-gray-800">
              <th className="border border-gray-300 px-4 py-2">ID</th>
              <th className="border border-gray-300 px-4 py-2">Nombre</th>
              <th className="border border-gray-300 px-4 py-2">Categoría</th>
              <th className="border border-gray-300 px-4 py-2">Monto mínimo</th>
            </tr>
          </thead>
          <tbody>
            {fondos.map((fondo) => (
              <tr key={fondo.id} className="hover:bg-gray-50 dark:hover:bg-gray-900">
                <td className="border border-gray-300 px-4 py-2">{fondo.id}</td>
                <td className="border border-gray-300 px-4 py-2">{fondo.nombre}</td>
                <td className="border border-gray-300 px-4 py-2">{fondo.categoria}</td>
                <td className="border border-gray-300 px-4 py-2">
                  {fondo.monto_minimo.toLocaleString("es-CO", {
                    style: "currency",
                    currency: "COP",
                  })}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </main>
  );
}
