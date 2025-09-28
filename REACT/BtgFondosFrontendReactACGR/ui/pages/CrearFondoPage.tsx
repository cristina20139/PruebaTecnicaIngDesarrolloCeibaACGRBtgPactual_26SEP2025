import { useState } from "react";
import { registrarFondo } from "../../application/usecases/CrearFondo";
import type { Fondo } from "../../domain/entidades/Fondo";

export default function CrearFondoPage() {
  const [nombre, setNombre] = useState("");
  const [monto, setMonto] = useState(0);
  const [categoria, setCategoria] = useState("");
  const [resultado, setResultado] = useState<Fondo | null>(null);
  const [error, setError] = useState(""); // mensaje proveniente del backend

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(""); // limpiar errores previos

    try {
      const nuevoFondo = await registrarFondo({
        nombre,
        monto_minimo: monto, // debe coincidir exactamente con el modelo del backend
        categoria,
      });
      setResultado(nuevoFondo);
    } catch (err: any) {
      // ⚡ Capturamos el mensaje exacto del backend
      if (err.response?.data?.detail) {
        // Para errores de Pydantic (422)
        if (Array.isArray(err.response.data.detail)) {
          setError(err.response.data.detail.map((d: any) => d.msg).join(", "));
        } else {
          setError(err.response.data.detail);
        }
      } else {
        // Para otros errores
        setError(err.message || "Error al crear fondo");
      }
    }
  };

  return (
    <main className="p-6">
      <h1 className="text-2xl font-bold mb-4">Crear Fondo</h1>

      <form onSubmit={handleSubmit} className="flex flex-col gap-3 max-w-sm">
        <input
          type="text"
          placeholder="Nombre del fondo"
          value={nombre}
          onChange={(e) => setNombre(e.target.value)}
          className="border p-2"
          required
        />

        <input
          type="number"
          placeholder="Monto mínimo"
          value={monto}
          onChange={(e) => setMonto(Number(e.target.value))}
          className="border p-2"
          required
        />

        <input
          type="text"
          placeholder="Categoría"
          value={categoria}
          onChange={(e) => setCategoria(e.target.value)}
          className="border p-2"
          required
        />

        {error && (
          <p className="text-red-600 text-sm font-medium">{error}</p>
        )}

        <button type="submit" className="bg-blue-600 text-white p-2 rounded">
          Crear Fondo
        </button>
      </form>

      {resultado && (
        <div className="mt-4 p-3 border rounded">
          <h2 className="font-bold">Fondo creado:</h2>
          <p>ID: {resultado.id}</p>
          <p>Nombre: {resultado.nombre}</p>
          <p>Categoría: {resultado.categoria}</p>
          <p>
            Monto mínimo:{" "}
            {resultado.monto_minimo.toLocaleString("es-CO", {
              style: "currency",
              currency: "COP",
            })}
          </p>
        </div>
      )}
    </main>
  );
}
