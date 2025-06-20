import { useEffect, useState } from "react";
import api from "../services/api";

export default function Orders() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    api.get("/orders").then((res) => setOrders(res.data));
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl mb-4">Pedidos</h1>
      <ul>
        {orders.map((o) => (
          <li key={o.id}>
            {o.item} - Quantidade: {o.quantity}
          </li>
        ))}
      </ul>
    </div>
  );
}
