import React from "react";

const RoadmapCard = ({ epic }) => {
  return (
    <div className="bg-white shadow-md rounded-2xl p-4 hover:shadow-xl transition">
      <h3 className="font-bold text-blue-600 mb-2">{epic.title}</h3>
      <ul className="list-disc list-inside text-gray-700 space-y-1">
        {epic.user_stories.map((us, idx) => (
          <li key={idx}>{us}</li>
        ))}
      </ul>
    </div>
  );
};

export default RoadmapCard;