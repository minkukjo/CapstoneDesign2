module.exports = (sequelize, DataTypes) =>
  sequelize.define(
    "order",
    {
      content: {
        type: DataTypes.STRING(500),
        allowNull: false
      }
    },
    {
      timestamps: true,
      paranoid: true,
      charset: "utf8",
      collate: "utf8_general_ci"
    }
  );
