import { useState } from "react";
import { registrarSuscripcion } from "../../application/usecases/SuscribirFondo";

export default function SuscribirFondoPage() {
  const [clienteId, setClienteId] = useState(0);
  const [fondoId, setFondoId] = useState(1); // ahora editable
  const [monto, setMonto] = useState(0);
  const [resultado, setResultado] = useState<any>(null);
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    try {
      const suscripcion = await registrarSuscripcion(fondoId, {
        cliente_id: clienteId,
        monto,
      });
      setResultado(suscripcion);
    } catch (err: any) {
      setError(err.response?.data?.detail || err.message || "Error al suscribirse");
    }
  };

  return (
    <main className="p-6">
      <h1 className="text-2xl font-bold mb-4">Suscribirse a Fondo</h1>

      <form onSubmit={handleSubmit} className="flex flex-col gap-3 max-w-sm">
        <label className="font-medium">ID Cliente:</label>
        <input
          type="number"
          placeholder="Ingrese ID Cliente"
          value={clienteId}
          onChange={(e) => setClienteId(Number(e.target.value))}
          className="border p-2"
          required
        />

        <label className="font-medium">ID Fondo:</label>
        <input
          type="number"
          placeholder="Ingrese ID Fondo"
          value={fondoId}
          onChange={(e) => setFondoId(Number(e.target.value))}
          className="border p-2"
          required
        />

        <label className="font-medium">Monto:</label>
        <input
          type="number"
          placeholder="Ingrese monto"
          value={monto}
          onChange={(e) => setMonto(Number(e.target.value))}
          className="border p-2"
          required
        />

        <button type="submit" className="bg-green-600 text-white p-2 rounded">
          Suscribirse
        </button>
      </form>

      {error && <p className="text-red-600 mt-2">{error}</p>}

      {resultado && (
        <div className="mt-4 p-3 border rounded">
          <h2 className="font-bold">Suscripción exitosa:</h2>
          <p>Cliente ID: {resultado.cliente_id}</p>
          <p>Fondo ID: {resultado.fondo_id}</p>
          <p>
            Monto:{" "}
            {resultado.monto.toLocaleString("es-CO", {
              style: "currency",
              currency: "COP",
            })}
          </p>
          <p>Tipo: {resultado.tipo}</p>
          <p>Fecha: {new Date(resultado.fecha).toLocaleString()}</p>
        </div>
      )}
    </main>
  );
}
